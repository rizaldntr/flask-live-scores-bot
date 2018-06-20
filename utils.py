def flex_today_matches_builder(home_team, away_team, home_goals, away_goals, time, home_code, away_code):
    picture_image_uri='https://api.fifa.com/api/v1/picture/flags-fwc2018-4/'
    return {
        "type": "flex",
        "altText": "WC18 - Today Matches",
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
                                "url": "{}{}".format(picture_image_uri, home_code)
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
                                "url": "{}{}".format(picture_image_uri, away_code)
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
