#!/bin/bash

# 1. Print a cool welcome message
echo "🚀 Installing Shatab's FastAPI + MongoDB Boilerplate..."

# 2. Clone the repository (replace with your actual repo link)
# The "$1" allows the user to pass a custom folder name, defaulting to "fastapi-app" if they don't
TARGET_DIR=${1:-fastapi-app}
git clone https://github.com/your-username/your-repo-name.git $TARGET_DIR

# 3. Navigate into the new folder
cd $TARGET_DIR

# 4. Set up the environment variables
if [ -f .env.example ]; then
    cp .env.example .env
    echo "📝 Copied .env.example to .env (Don't forget to update your secrets!)"
fi

# 5. Print the final instructions
echo ""
echo "✅ Installation Complete!"
echo "👉 Next steps:"
echo "   cd $TARGET_DIR"
echo "   python -m venv venv"
echo "   source venv/Scripts/activate  # (or venv/bin/activate on Mac/Linux)"
echo "   pip install -r requirements.txt"