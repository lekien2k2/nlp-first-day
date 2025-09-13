# Định nghĩa luật và fallbacks
RULES = [
    {
        "keywords": ["mon hoc nay", "mon nlp", "mon xu ly ngon ngu", "subject", "course nlp", "mon hoc xu ly ngon ngu tu nhien", "mon nay"],
        "answer": "Môn học Xử lý ngôn ngữ tự nhiên (NLP) giới thiệu về cách máy tính hiểu và xử lý ngôn ngữ con người."
    },
    {
        "keywords": ["kien thuc can co", "prerequisites", "background knowledge", "nen biet gi", "can chuan bi gi", "kien thuc nen co", "kien thuc tien quyet", "can hoc gi truoc"],
        "answer": "Bạn nên nắm vững kiến thức về đại số tuyến tính, xác suất thống kê và lập trình."
    },
    {
        "keywords": ["nlp la gi", "what is nlp", "define nlp", "dinh nghia nlp", "natural language processing la gi", "xu ly ngon ngu tu nhien la gi", "nlp?", "giai thich nlp"],
        "answer": "NLP là một lĩnh vực của Trí tuệ nhân tạo, giao thoa giữa Ngôn ngữ học và Khoa học máy tính."
    },
    {
        "keywords": ["ung dung nlp", "applications", "nlp dung lam gi", "practical uses", "use cases", "ung dung thuc te", "nlp applications", "ap dung nlp", "ung dung thuc te"],
        "answer": "Các ứng dụng của NLP bao gồm dịch máy, phân tích cảm xúc, chatbot và nhận dạng giọng nói."
    },
    {
        "keywords": ["thuat toan", "algorithms", "models", "mo hinh", "techniques", "ky thuat", "phuong phap", "thuat toan nlp", "mo hinh nlp"],
        "answer": "Một số thuật toán phổ biến trong NLP là N-gram, HMM, LSTM, và Transformer."
    },
    {
        "keywords": ["sach", "giao trinh", "textbook", "book", "tai lieu tham khao", "reference", "doc sach gi", "sach hay", "sach nlp"],
        "answer": "Bạn có thể tham khảo sách \"Speech and Language Processing\" của Jurafsky & Martin."
    },
    {
        "keywords": ["thu vien", "library", "framework", "cong cu", "tools", "thu vien lap trinh", "programming libraries", "code nlp", "thu vien nlp"],
        "answer": "Các thư viện lập trình phổ biến nhất là NLTK, spaCy, và Hugging Face Transformers."
    },
    {
        "keywords": ["bai tap", "assignments", "homework", "projects", "practice", "thuc hanh", "lab", "bai tap ve nha", "project"],
        "answer": "Bài tập của môn học thường bao gồm xây dựng các mô hình như phân loại văn bản và nhận dạng thực thể."
    },
    {
        "keywords": ["muc tieu", "objectives", "goals", "purpose", "learning outcomes", "ket qua hoc tap", "mong doi", "muc dich"],
        "answer": "Mục tiêu của môn học là giúp sinh viên nắm được lý thuyết nền tảng và các ứng dụng thực tế của NLP."
    },
    {
        "keywords": ["tai lieu", "materials", "lecture notes", "slides", "resources", "hoc lieu", "tai lieu hoc tap", "giao trinh", "slide"],
        "answer": "Tất cả tài liệu học tập đều có trên hệ thống LMS của trường."
    }
]

FALLBACKS = [
    "Mình chưa hiểu câu hỏi. Bạn có thể diễn đạt khác hoặc rút gọn giúp mình không?",
    "Xin lỗi, mình chưa có luật cho câu hỏi này. Bạn thử hỏi cụ thể hơn nhé!",
    "Mình chưa có thông tin phù hợp. Bạn thêm ngữ cảnh hoặc từ khóa khác giúp mình nha."
]