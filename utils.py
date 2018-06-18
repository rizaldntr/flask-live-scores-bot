def flex_today_matches_builder(home_team, away_team, home_goals, away_goals, time):
    return {
        "type":"flex",
        "altText":"WC18 - Today Matches",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_1.png"
                    },
                    {
                        "type": "text",
                        "text": "{} - {}".format(home_goals, away_goals),
                        "gravity": "center",
                        "align": "center",
                        "size": "xxl"
                    },
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_1.png"
                    }
                    ]
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": home_team,
                        "gravity": "center",
                        "align": "center",
                        "size": "sm",
                        "wrap": True
                    },
                    {
                        "type": "text",
                        "text": time,
                        "gravity": "center",
                        "align": "center",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": away_team,
                        "gravity": "center",
                        "align": "center",
                        "size": "sm",
                        "wrap": True
                    }
                    ]
                },
                {
                    "type": "separator",
                    "margin": "lg"
                }
                ]
            }
        }
    }