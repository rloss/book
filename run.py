from app import create_app

# 앱 인스턴스 생성 (환경 설정 포함됨)
app = create_app()

if __name__ == "__main__":
    app.run()
