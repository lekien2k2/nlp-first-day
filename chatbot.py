import re
import unicodedata
from difflib import SequenceMatcher
from typing import Dict, List, Optional

class NLPRuleBot:
    def __init__(self, rules: List[Dict], fallbacks: List[str], similarity_threshold: float = 0.88):
        """
        Khởi tạo chatbot với các luật và câu trả lời mặc định
        Args:
            rules: Danh sách các luật (keywords và answer)
            fallbacks: Danh sách câu trả lời khi không tìm thấy luật phù hợp
            similarity_threshold: Ngưỡng độ tương đồng cho khớp mờ
        """
        self.rules = rules
        self.fallbacks = fallbacks
        self.similarity_threshold = similarity_threshold
        # Chuẩn hóa keywords trước để tối ưu performance
        self.normalized_rules = self._preprocess_rules()

    @staticmethod
    def normalize_text(text: str) -> str:
        """Chuẩn hóa văn bản: lowercase, bỏ dấu, chuẩn hóa khoảng trắng."""
        # Chuyển thành lowercase và xóa khoảng trắng thừa
        text = text.lower().strip()
        # Bỏ dấu tiếng Việt
        text = ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )
        # Thay nhiều khoảng trắng bằng một khoảng trắng
        return re.sub(r'\s+', ' ', text)

    def _preprocess_rules(self) -> List[Dict]:
        """Tiền xử lý và chuẩn hóa keywords của các luật."""
        normalized = []
        for rule in self.rules:
            # Chuẩn hóa tất cả keywords trong luật
            norm_keywords = [self.normalize_text(kw) for kw in rule["keywords"]]
            normalized.append({
                "keywords": norm_keywords,
                "answer": rule["answer"]
            })
        return normalized

    def _find_best_match(self, input_text: str) -> Optional[str]:
        """
        Tìm luật phù hợp nhất với câu hỏi của người dùng.
        Returns:
            Câu trả lời cho luật phù hợp nhất hoặc None nếu không tìm thấy
        """
        best_ratio = 0
        best_answer = None
        
        norm_input = self.normalize_text(input_text)
        
        for rule in self.normalized_rules:
            for keyword in rule["keywords"]:
                # Ưu tiên khớp chính xác
                if keyword in norm_input:
                    return rule["answer"]
                
                # Nếu không khớp chính xác, tính độ tương đồng
                ratio = SequenceMatcher(None, norm_input, keyword).ratio()
                if ratio > best_ratio and ratio >= self.similarity_threshold:
                    best_ratio = ratio
                    best_answer = rule["answer"]
        
        return best_answer

    def reply(self, user_input: str) -> str:
        """
        Xử lý câu hỏi và trả về câu trả lời phù hợp.
        Args:
            user_input: Câu hỏi của người dùng
        Returns:
            Câu trả lời từ luật phù hợp hoặc fallback
        """
        if not user_input.strip():
            return "Bạn chưa nhập câu hỏi!"
            
        answer = self._find_best_match(user_input)
        if answer:
            return answer
            
        # Trả về ngẫu nhiên một câu fallback
        import random
        return random.choice(self.fallbacks)

def main():
    from rules import RULES, FALLBACKS  # Import từ file riêng
    
    # Khởi tạo chatbot
    bot = NLPRuleBot(RULES, FALLBACKS)
    
    print("🤖 NLP RuleBot - Gõ 'exit' để thoát")
    
    while True:
        try:
            user_input = input("Bạn: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in {"exit", "quit"}:
                print("Tạm biệt!")
                break
                
            print("Bot:", bot.reply(user_input))
            
        except (EOFError, KeyboardInterrupt):
            print("\nTạm biệt!")
            break

if __name__ == "__main__":
    main()