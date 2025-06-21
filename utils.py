def detect_trend_patterns(df):
    result = df["Result"].tolist()
    biet = any(result[i] == result[i+1] == result[i+2] for i in range(len(result)-2))
    trap = any(result[i:i+4] == ["P","B","P","B"] for i in range(len(result)-3))

    if biet and trap:
        return "cầu bệt + tráo"
    elif biet:
        return "bệt"
    elif trap:
        return "tráo"
    else:
        return "không rõ"
