# Translation data for the portfolio website
# 中英文切換功能的翻譯資料

TRANSLATIONS = {
    'en': {
        'nav': {
            'about': 'About',
            'experience': 'Experience',
            'education': 'Education',
            'skills': 'Skills',
            'projects': 'Projects',
            'certifications': 'Certifications',
            'github': 'GitHub',
            'contact': 'Contact'
        },
        'hero': {
            'title': 'AI Engineer & Data Scientist',
            'get_in_touch': 'Get In Touch',
            'download_resume': 'Download Resume',
            'location': 'Taipei, Taiwan'
        },
        'about': {
            'title': 'About Me',
            'description':
            'I am an experienced AI Engineer with a strong background in mathematical modeling and software development. My expertise spans across machine learning, computer vision, and deep learning applications, with proven experience in building AI chatbots, recommendation systems, and data analysis platforms.',
            'education_label': 'Education',
            'education_desc':
            "Master's in Economics\nBachelor's in Mathematics",
            'experience_label': 'Experience',
            'experience_desc': '1+ Years in AI Engineering\n& Data Science',
            'certifications_label': 'Certifications',
            'certifications_desc': 'Google Cybersecurity\nIBM AI Engineering'
        },
        'experience': {
            'title': 'Work Experience'
        },
        'education': {
            'title': 'Education'
        },
        'skills': {
            'title': 'Technical Skills'
        },
        'projects': {
            'title': 'Featured Projects',
            'key_features': 'Key Features:'
        },
        'certifications': {
            'title': 'Certifications',
            'verify': 'Verify'
        },
        'github': {
            'title': 'GitHub Projects',
            'repositories': 'Repositories',
            'followers': 'Followers',
            'following': 'Following',
            'visit_profile': 'Visit GitHub Profile',
            'no_repos': 'Unable to load GitHub repositories at this time.'
        },
        'contact': {
            'title': 'Contact Information',
            'info': 'Contact Information',
            'github_profile': 'GitHub Profile'
        },
        'footer': {
            'rights': 'All rights reserved.'
        }
    },
    'zh': {
        'nav': {
            'about': '關於我',
            'experience': '工作經歷',
            'education': '教育背景',
            'skills': '技能',
            'projects': '專案',
            'certifications': '證照',
            'github': 'GitHub',
            'contact': '聯絡我'
        },
        'hero': {
            'title': 'AI工程師與資料科學家',
            'get_in_touch': '聯絡我',
            'download_resume': '下載履歷',
            'location': '台北，台灣'
        },
        'about': {
            'title': '關於我',
            'description':
            '我是一位新進的AI工程師，具有強大的數學建模和軟體開發背景。我的專業領域涵蓋機器學習、電腦視覺和深度學習應用，在建立AI聊天機器人、推薦系統和資料分析平台方面有豐富的經驗。',
            'education_label': '教育背景',
            'education_desc': '經濟學碩士\n數學學士',
            'experience_label': '工作經驗',
            'experience_desc': '1年以上AI工程師\n與資料科學經驗',
            'certifications_label': '專業證照',
            'certifications_desc': 'Google網路安全\nIBM AI工程師'
        },
        'experience': {
            'title': '工作經歷'
        },
        'education': {
            'title': '教育背景'
        },
        'skills': {
            'title': '技術技能'
        },
        'projects': {
            'title': '精選專案',
            'key_features': '主要功能：'
        },
        'certifications': {
            'title': '專業證照',
            'verify': '驗證'
        },
        'github': {
            'title': 'GitHub專案',
            'repositories': '儲存庫',
            'followers': '追蹤者',
            'following': '追蹤中',
            'visit_profile': '訪問GitHub個人資料',
            'no_repos': '目前無法載入GitHub儲存庫。'
        },
        'contact': {
            'title': '聯絡資訊',
            'info': '聯絡資訊',
            'github_profile': 'GitHub個人資料'
        },
        'footer': {
            'rights': '版權所有。'
        }
    }
}

# Personal info translations
PERSONAL_INFO_TRANSLATIONS = {
    'en': {
        'name': 'Ming-Hsuan Hsu',
        'chinese_name': '許銘軒',
        'title': 'AI Engineer & Data Scientist',
        'location': 'Taipei, Taiwan',
        'phone': '0972-143-390',
        'email': 'minghsuanhsu.workspace@gmail.com',
        'summary': 'Experienced AI Engineer with strong background in mathematical modeling and software development. Skilled in Python, TensorFlow, PyTorch, and computer vision. Proven track record in AI application development, research, and cross-functional collaboration.'
    },
    'zh': {
        'name': '許銘軒',
        'chinese_name': 'Ming-Hsuan Hsu',
        'title': 'AI工程師與資料科學家',
        'location': '台北，台灣',
        'phone': '0972-143-390',
        'email': 'minghsuanhsu.workspace@gmail.com',
        'summary': '新進的AI工程師，具數學建模，資料分析背景。熟練使用Python、TensorFlow、PyTorch和電腦視覺技術。有AI應用開發、研究和跨域協作的經驗。'
    }
}

# Work experience translations
WORK_EXPERIENCE_TRANSLATIONS = {
    'en': [{
        'title': 'AI Engineer',
        'company': 'Deepinsight Company',
        'period': '2024/09 - 2024/11',
        'location': 'Taipei',
        'responsibilities': [
            'Built AI chatbot systems integrating online large language models',
            'Managed cloud services for client usage and NoSQL database integration',
            'Optimized bot delivery system using Azure queue system, reducing delivery time by 90%'
        ],
        'technologies': ['AI', 'LLM', 'Cloud Services', 'PostgreSQL', 'Azure']
    }, {
        'title': 'Campaign Director',
        'company': 'Taitung County Legislative Candidate Campaign',
        'period': '2023/06 - 2024/02',
        'location': 'Taitung',
        'responsibilities': [
            'Organized policies across six domains and charted election campaigns',
            'Delivered street presentations dozens of times',
            'Coordinated between candidate vision and team execution'
        ],
        'technologies': ['Project Management', 'Public Speaking', 'Strategic Planning']
    }, {
        'title': 'Research Assistant',
        'company': 'Academia Sinica',
        'period': '2021/06 - 2022/07',
        'location': 'Taipei',
        'responsibilities': [
            'Conducted cooperative game theory research',
            'Studied mechanism design between non-cooperative and cooperative game theory',
            'Integrated data from multiple public databases for Taiwan-Korea economic comparison'
        ],
        'technologies': ['Python', 'Data Analysis', 'Research', 'Statistical Modeling']
    }],
    'zh': [{
        'title': 'AI工程師',
        'company': '深義分析股份有限公司',
        'period': '2024/09 - 2024/11',
        'location': '台北',
        'responsibilities': [
            '建立整合線上大型語言模型的AI聊天機器人系統',
            '管理客戶使用的雲端服務及NoSQL資料庫整合',
            '使用Azure佇列系統優化機器人投遞系統，減少90%投遞時間'
        ],
        'technologies': ['AI', '大型語言模型', '雲端服務', 'PostgreSQL', 'Azure']
    }, {
        'title': '競選總幹事',
        'company': '台東縣區域立委候選人許瑞貴競選團隊',
        'period': '2023/06 - 2024/02',
        'location': '台東',
        'responsibilities': [
            '統籌六大政策領域並制定選舉策略',
            '進行數十場街頭演講',
            '協調候選人願景與團隊執行'
        ],
        'technologies': ['專案管理', '公開演講', '策略規劃']
    }, {
        'title': '研究助理',
        'company': '中央研究院',
        'period': '2021/06 - 2022/07',
        'location': '台北',
        'responsibilities': [
            '進行合作賽局理論研究',
            '研究非合作與合作賽局理論間的機制設計',
            '整合多個公開資料庫進行台韓經濟比較'
        ],
        'technologies': ['Python', '資料分析', '研究', '統計建模']
    }]
}

# Education translations
EDUCATION_TRANSLATIONS = {
    'en': [{
        'degree': 'Master of Economics',
        'institution': 'National Taiwan University',
        'period': '2018/02 - 2021/02',
        'specialization': 'Game Theory, Information Design, Network Theory'
    }, {
        'degree': 'Bachelor of Mathematics',
        'institution': 'National Taiwan University',
        'period': '2010/09 - 2014/06',
        'specialization': 'Mathematical Modeling, Statistics'
    }],
    'zh': [{
        'degree': '經濟學碩士',
        'institution': '國立臺灣大學',
        'period': '2018/02 - 2021/02',
        'specialization': '賽局理論、資訊設計、網絡理論'
    }, {
        'degree': '數學學士',
        'institution': '國立臺灣大學',
        'period': '2010/09 - 2014/06',
        'specialization': '數學建模、統計學'
    }]
}

# Skills translations
SKILLS_TRANSLATIONS = {
    'en': {
        'Programming Languages': ['Python', 'SQL', 'JavaScript', 'R'],
        'AI/ML Frameworks':
        ['TensorFlow', 'PyTorch', 'scikit-learn', 'OpenCV'],
        'Cloud & Databases': ['Azure', 'PostgreSQL', 'MongoDB', 'MySQL'],
        'Tools & Technologies':
        ['Docker', 'Linux', 'Git', 'Jupyter', 'Arduino'],
        'Research & Analysis': [
            'Mathematical Modeling', 'Game Theory', 'Statistical Analysis',
            'Data Visualization'
        ]
    },
    'zh': {
        '程式語言': ['Python', 'SQL', 'JavaScript', 'R'],
        'AI/ML框架': ['TensorFlow', 'PyTorch', 'scikit-learn', 'OpenCV'],
        '雲端與資料庫': ['Azure', 'PostgreSQL', 'MongoDB', 'MySQL'],
        '工具與技術': ['Docker', 'Linux', 'Git', 'Jupyter', 'Arduino'],
        '研究與分析': ['數學建模', '賽局理論', '統計分析', '資料視覺化']
    }
}

# Projects translations
PROJECTS_TRANSLATIONS = {
    'en': [{
        'title':
        'AI Face Recognition Makeup Recommendation System',
        'period':
        '2024/06 - 2024/07',
        'description':
        'Developed an AI-powered makeup recommendation system using computer vision and deep learning',
        'technologies': [
            'Python', 'OpenCV', 'mediaPipe', 'TensorFlow', 'DenseNet',
            'Autoencoder'
        ],
        'features': [
            'Face detection and analysis using OpenCV and mediaPipe',
            'Makeup area extraction using pyMatting background removal',
            'DenseNet-based Autoencoder for makeup simulation',
            'Personalized product recommendations based on facial features'
        ]
    }, {
        'title':
        'Podcast Production - Tristan\'s Imagination Time',
        'period':
        '2023/09 - Present',
        'description':
        'Created and produced 92 episodes of career exploration and economic analysis podcast',
        'technologies': ['Audio Production', 'Content Creation', 'Marketing'],
        'features': [
            'Career exploration and economic theory application',
            'Cross-disciplinary content covering psychology and politics',
            'Achieved above-median performance on Firstory platform'
        ]
    }],
    'zh': [{
        'title':
        'AI人臉辨識化妝品推薦系統',
        'period':
        '2024/06 - 2024/07',
        'description':
        '使用電腦視覺和深度學習技術開發AI化妝品推薦系統',
        'technologies': [
            'Python', 'OpenCV', 'mediaPipe', 'TensorFlow', 'DenseNet',
            'Autoencoder'
        ],
        'features': [
            '使用OpenCV和mediaPipe進行人臉偵測和分析', '使用pyMatting背景移除技術提取化妝區域',
            '基於DenseNet的自編碼器進行化妝模擬', '根據面部特徵提供個人化產品推薦'
        ]
    }, {
        'title':
        'Podcast製作 - 崔斯坦的異想時間',
        'period':
        '2023/09 - 現在',
        'description':
        '創作並製作了92集職涯探索和經濟分析的播客節目',
        'technologies': ['音頻製作', '內容創作', '行銷'],
        'features': ['職涯探索和經濟理論應用', '跨領域內容涵蓋心理學和政治', '在Firstory平台上達到超過中位數的表現']
    }]
}

# Certifications translations
CERTIFICATIONS_TRANSLATIONS = {
    'en': [{
        'name':
        'Google Cybersecurity Professional Certificate',
        'issuer':
        'Google',
        'date':
        'May 2025',
        'credential_id':
        'KHBPLQNO5MX0',
        'verify_url':
        'https://coursera.org/verify/professional-cert/KHBPLQNO5MX0',
        'description':
        'Completed 8 courses covering cybersecurity fundamentals, network security, Linux, SQL, and Python automation'
    }, {
        'name':
        'IBM AI Engineering Professional Certificate',
        'issuer':
        'IBM',
        'date':
        'June 2025',
        'credential_id':
        'LWJRN28JENKF',
        'verify_url':
        'https://coursera.org/verify/professional-cert/LWJRN28JENKF',
        'description':
        'Mastered deep learning, neural networks, and LLMs using Keras, PyTorch, and TensorFlow'
    }],
    'zh': [{
        'name': 'Google網路安全專業證書',
        'issuer': 'Google',
        'date': '2025年5月',
        'credential_id': 'KHBPLQNO5MX0',
        'verify_url':
        'https://coursera.org/verify/professional-cert/KHBPLQNO5MX0',
        'description': '完成8門課程，涵蓋網路安全基礎、網路安全、Linux、SQL和Python自動化'
    }, {
        'name': 'IBM AI工程師專業證書',
        'issuer': 'IBM',
        'date': '2025年6月',
        'credential_id': 'LWJRN28JENKF',
        'verify_url':
        'https://coursera.org/verify/professional-cert/LWJRN28JENKF',
        'description': '掌握深度學習、神經網路和大型語言模型，使用Keras、PyTorch和TensorFlow'
    }]
}
