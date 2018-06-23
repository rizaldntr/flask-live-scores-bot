def build_group_result(letter):
    country = []
    points = []
    wins = []
    draws = []
    losses = []
    game_played = []
    goal_differential = []

def build_goal_by_content(home_team_events, away_team_events):
    home_scorer = []
    away_scorer = []

    for data in home_team_events:
        if data['type_of_event'] == 'goal':

            scorer = data['player']
            scorer = scorer.split(' ')[-1]
            time = data['time']

            temp = {
                "type": "text",
                "text": ' ' + time + ' ' + scorer,
                "gravity": "center",
                "align": "start",
                "size": "sm",
                "wrap": True
            }

            home_scorer.append(temp)

    for data in away_team_events:
        if data['type_of_event'] == 'goal':

            scorer = data['player']
            scorer = scorer.split(' ')[-1]
            time = data['time']

            temp = {
                "type": "text",
                "text": scorer + ' ' + time + ' ',
                "gravity": "center",
                "align": "end",
                "size": "sm",
                "wrap": True
            }

            away_scorer.append(temp)

    temp = {
            "type": "text",
            "text": "-",
            "gravity": "center",
            "align": "center",
            "size": "md",
            "wrap": True
        }
        
    if len(home_scorer) == 0:
        home_scorer.append(temp)

    if len(away_scorer) == 0:
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
                        "margin": "lg",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "md",
                                "contents": home_scorer
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "md",
                                "contents": away_scorer
                            }
                        ]
                    }
                ]
            }
        }
    }

def flex_help_message_builder():
    return {
        "type": "flex",
        "altText": "WC18 - Command Help",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "COMMAND FORMAT",
                        "weight": "bold",
                        "color": "#1DB446",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "/wc18<space><command>",
                        "weight": "bold",
                        "size": "md",
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "today",
                                        "weight": "bold",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "display today's matches",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "current",
                                        "weight": "bold",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "display current match",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "start live",
                                        "weight": "bold",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "start live score notification",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "stop live",
                                        "weight": "bold",
                                        "size": "sm",
                                        "color": "#555555",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "stop live score notification",
                                        "size": "sm",
                                        "color": "#111111",
                                        "align": "end"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }
