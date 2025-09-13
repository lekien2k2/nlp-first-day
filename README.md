# NLP Rule-Based Chatbot 🤖

Một chatbot đơn giản trả lời các câu hỏi về Xử lý Ngôn ngữ Tự nhiên (NLP) dựa trên luật, hỗ trợ cả tiếng Việt và tiếng Anh.

## Thành viên nhóm

| Họ và tên | MSSV |
|-----------|------|
| Lê Tấn Kiên | 2591309 |
| Đỗ Quốc Khánh | 2591307 |
| Nguyễn Trương Hoàng Hiếu | 2591304 |

## Mục tiêu

- Xây dựng chatbot rule-based cho lĩnh vực lớp học NLP
- Hỗ trợ nhận diện câu hỏi bằng từ khóa tiếng Việt & tiếng Anh
- Cung cấp câu trả lời bằng tiếng Việt
- Áp dụng cách tiếp cận rule-based trong NLP

## Tính năng chính

- **Hỗ trợ đa ngôn ngữ**: Nhận câu hỏi bằng tiếng Việt hoặc tiếng Anh
- **Xử lý mờ**: Chấp nhận lỗi chính tả nhẹ và các cách diễn đạt khác nhau
- **Cơ chế fallback**: Trả lời thân thiện khi không tìm thấy luật phù hợp
- **20+ luật tích hợp**: Bao gồm các khái niệm NLP cơ bản và nâng cao

## Các chủ đề được hỗ trợ

1. **Thông tin môn học**:
   - Giới thiệu và định nghĩa NLP
   - Mục tiêu và kết quả học tập
   - Kiến thức tiên quyết (đại số, xác suất, lập trình)

2. **Tài nguyên học tập**:
   - Sách và tài liệu tham khảo
   - Thư viện lập trình (NLTK, spaCy, Hugging Face)
   - Tài liệu giảng dạy trên LMS

3. **Kiến thức chuyên môn**:
   - Thuật toán cơ bản (N-gram, HMM, LSTM)
   - Mô hình hiện đại (Transformer)
   - Bài tập thực hành

4. **Ứng dụng thực tế**:
   - Dịch máy (Machine Translation)
   - Phân tích cảm xúc (Sentiment Analysis)
   - Chatbot và trợ lý ảo
   - Nhận dạng giọng nói (ASR)

## 🛠️ Cài đặt và Sử dụng

### Yêu cầu
- Python 3.6+
- Không cần thư viện phụ thuộc bổ sung

### Cài đặt
```bash
git clone https://github.com/lekien2k2/nlp-first-day.git
cd nlp-first-day
```

### Chạy chatbot
```bash
python buoi-1/chatbot_optimized.py  # Phiên bản tối ưu
```

## 💬 Ví dụ sử dụng

```
Bạn: NLP là gì?
Bot: NLP (Xử lý ngôn ngữ tự nhiên) là lĩnh vực giúp máy tính hiểu, sinh và tương tác bằng ngôn ngữ con người.

Bạn: What is tokenization?
Bot: Tokenization là bước tách văn bản thành đơn vị nhỏ (từ hoặc subword) để mô hình có thể xử lý.

Bạn: Cho mình biết về BERT
Bot: BERT là mô hình mã hóa hai chiều mạnh, dùng cho phân loại, NER, QA (thường fine-tune theo tác vụ).
```

## ⚠️ Hạn chế hiện tại

1. **Từ đồng nghĩa**: Chỉ nhận diện các từ khóa đã được định nghĩa
2. **Lỗi chính tả**: Chỉ xử lý được các lỗi nhỏ, không xử lý được lỗi lớn
3. **Phạm vi hạn chế**: Chỉ trả lời được các câu hỏi trong phạm vi luật
4. **Khó mở rộng**: Cần thêm luật thủ công khi muốn mở rộng kiến thức

## 🔄 Cải tiến tương lai

1. Thêm xử lý từ đồng nghĩa tự động
2. Cải thiện khả năng chịu lỗi chính tả
3. Tích hợp với mô hình ngôn ngữ để trả lời linh hoạt hơn
4. Thêm khả năng học từ tương tác với người dùng

## 📝 Tài liệu tham khảo

1. [Natural Language Processing with Python](https://www.nltk.org/book/)
2. [Rule-based NLP Systems](https://web.stanford.edu/~jurafsky/slp3/)
3. [Building Chatbots in Python](https://www.datacamp.com/courses/building-chatbots-in-python)