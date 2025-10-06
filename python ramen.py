import random
import sys

# 問題データリスト
# 【重要】ご自身で画像を検索し、URLを貼り付けて問題を完成させてください。
# 画像はブラウザで直接開いて確認しながら遊ぶことを想定しています。
quiz_data = [
    {
        # 一蘭のとんこつラーメン画像（検索結果）
        "url": "http://googleusercontent.com/image_collection/image_retrieval/11748455279520892921_0",
        "answer": "一蘭",
        "hint": "赤い秘伝のタレと『味集中カウンター』が特徴のチェーン店。"
    },
    {
        # 【ここに「博多一風堂」の画像URLを挿入】
        "url": "【博多一風堂の画像URL】",
        "answer": "博多一風堂",
        "hint": "『赤丸新味』と『白丸元味』の2種類が有名なグローバルチェーン。"
    },
    {
        # 【ここに「ラーメン山岡家」の画像URLを挿入】
        "url": "【ラーメン山岡家の画像URL】",
        "answer": "ラーメン山岡家",
        "hint": "独特の豚骨臭と24時間営業で知られるチェーン店。"
    },
    {
        # --- ここから追加した問題 ---
        # 【ここに「天下一品」のこってりラーメン画像URLを挿入】
        "url": "【天下一品の画像URL】",
        "answer": "天下一品",
        "hint": "『こってり』スープが泥のように濃厚なことで有名なチェーン店。"
    },
    {
        # 【ここに「日高屋」の中華そば画像URLを挿入】
        "url": "【日高屋の画像URL】",
        "answer": "日高屋",
        "hint": "低価格で『中華そば』や餃子を提供する、駅前によくある中華食堂チェーン。"
    }
]

def ramen_quiz_game():
    """チェーン店ラーメン当てクイズを実行する関数"""
    print(" チェーン店ラーメン当てクイズゲーム ") # タイトル変更
    print("表示された画像URLをブラウザで開き、どこの店のラーメンか当ててください！")
    print("回答は全角・半角を問わず、『一蘭』や『天下一品』のように店名のみを入力してください。")
    print("-------------------------------------------------------")
    
    # 問題リストをシャッフル
    random.shuffle(quiz_data)
    
    score = 0
    
    # 問題数 (URLが未設定の問題を除外)
    available_questions = [q for q in quiz_data if '【' not in q['url'] and '】' not in q['url']]
    total_questions = len(available_questions)

    if total_questions == 0:
        print(" 全ての問題の画像URLが未設定のため、ゲームを開始できません。URLを設定してから再度実行してください。")
        return

    question_count = 0
    for question in quiz_data:
        # 画像URLがダミーのままの場合はスキップ
        if '【' in question['url'] or '】' in question['url']:
            continue

        question_count += 1
        print(f"\n--- 第 {question_count} 問 ---")
        print(f"このラーメンはどこのチェーン店のものでしょう？")
        print(f"画像のURL: {question['url']}") # 画像URLを提示
        print(f"ヒント: {question['hint']}") # ヒントを提示
        
        # ユーザーの解答を取得
        user_input = input("店名を入力してください ('quit'で終了): ")
        
        # 小文字化し、スペースを除去して比較しやすくする
        user_answer = user_input.strip().replace(' ', '').lower()
        correct_answer = question['answer'].strip().replace(' ', '').lower()
        
        # 終了判定
        if user_input.lower() == 'quit':
            print("\nゲームを中断します。")
            break
        
        # 正誤判定
        if user_answer == correct_answer:
            print(" 正解です！お見事！ ")
            score += 1
        else:
            print(f" 残念！不正解です。")
            print(f"正解は 【{question['answer']}】 でした。")
            
    # ゲーム終了時のスコア表示
    print("\n=======================================================")
    print(f" ゲーム終了！ あなたのスコアは {total_questions} 問中 {score} 点でした！ ")
    print("=======================================================")
    
# ゲーム開始
if __name__ == "__main__":
    ramen_quiz_game()
