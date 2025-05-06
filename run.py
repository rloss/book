import os
from app import create_app

app = create_app()

# Render 환경에서는 PORT 환경변수를 사용
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render에서 PORT는 자동 할당됨
    app.run(host="0.0.0.0", port=port, debug=True)
