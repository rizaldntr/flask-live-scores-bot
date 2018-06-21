def build_goal_by_content(home_team_events, away_team_events):
    home_scorer = []
    away_scorer = []

    for data in home_team_events:
        if data['type_of_event'] == 'goal':
            
            scorer = data['type_of_event']['player']
            scorer = scorer.split(' ')[-1]
            time = data['type_of_event']['time']

            temp = {
                "type": "text",
                "text": scorer + ' ' + time,
                "gravity": "center",
                "align": "left",
                "size": "sm",
                "wrap": True
            }

            home_scorer.append(temp)

    for data in away_team_events:
        if data['type_of_event'] == 'goal':
            
            scorer = data['type_of_event']['player']
            scorer = scorer.split(' ')[-1]
            time = data['type_of_event']['time']

            temp = {
                "type": "text",
                "text": scorer + ' ' + time,
                "gravity": "center",
                "align": "righht",
                "size": "sm",
                "wrap": True
            }

            away_scorer.append(temp)

    return home_scorer, away_scorer

def flex_today_matches_builder(home_team, away_team, home_goals, away_goals, time, home_code, away_code, home_team_events, away_team_events):
    picture_image_uri='https://api.fifa.com/api/v1/picture/flags-fwc2018-4/'
    home_scorer, away_scorer = build_goal_by_content(home_team_events, away_team_events)
    
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
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": home_scorer
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": away_scorer
                            }
                        ]
                    }
                ]
            }
        }
    }
