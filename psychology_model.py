import random

def analyze_psychology(history, trend_info):
    player_scores = []
    dealer_scores = []
    score = 0
    dealer_score = 0

    for outcome in history:
        if outcome == "P":
            score += 1
            dealer_score -= 0.5
        elif outcome == "B":
            score -= 1
            dealer_score += 1
        elif outcome == "T":
            score += 0.2
            dealer_score += 0.2
        player_scores.append(score)
        dealer_scores.append(dealer_score)

    player_type = "Liều lĩnh" if score > 3 else "Bảo thủ" if score < -2 else "Cân bằng"
    dealer_type = "Bẫy cầu" if dealer_score > 3 else "Dễ đoán" if dealer_score < -2 else "Trung lập"

    return {
        "player_type": player_type,
        "dealer_type": dealer_type,
        "player_score": round(score, 2),
        "dealer_score": round(dealer_score, 2),
        "player_scores": player_scores,
        "dealer_scores": dealer_scores,
        "player_strategy": "Nên phản cầu" if "bệt" in trend_info else "Theo chuỗi ngắn",
        "dealer_strategy": "Có dấu hiệu điều phối" if "tráo" in trend_info else "Không rõ mô hình"
    }

def predict_next_move(history, trend_info):
    if "bệt" in trend_info:
        last = history[-1]
        prediction = "B" if last == "P" else "P"
        confidence = 0.65
    elif "tráo" in trend_info:
        prediction = history[-2] if len(history) >= 2 else "P"
        confidence = 0.55
    else:
        prediction = random.choice(["P", "B"])
        confidence = 0.5
    return prediction, confidence

def win_rate_if_counter_trend(history):
    wins = 0
    total = 0
    for i in range(3, len(history)):
        prev = history[i-3:i]
        if all(p == prev[0] for p in prev):  # cầu bệt
            expected = "P" if prev[0] == "B" else "B"
            if history[i] == expected:
                wins += 1
            total += 1
    return round(wins / total, 2) if total > 0 else 0.5
