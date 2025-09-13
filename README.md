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
python chatbot.py  
```

## 💬 Ví dụ sử dụng

```
Bạn: Môn học này nói về gì?
Bot: Môn học Xử lý ngôn ngữ tự nhiên (NLP) giới thiệu về cách máy tính hiểu và xử lý ngôn ngữ con người.

Bạn: Cần những kiến thức gì để học môn này?
Bot: Bạn nên nắm vững kiến thức về đại số tuyến tính, xác suất thống kê và lập trình.

Bạn: What algorithms are used in NLP?
Bot: Một số thuật toán phổ biến trong NLP là N-gram, HMM, LSTM, và Transformer.

Bạn: Có thư viện nào để làm NLP không?
Bot: Các thư viện lập trình phổ biến nhất là NLTK, spaCy, và Hugging Face Transformers.

Bạn: Bài tập môn này như thế nào?
Bot: Bài tập của môn học thường bao gồm xây dựng các mô hình như phân loại văn bản và nhận dạng thực thể.
```

