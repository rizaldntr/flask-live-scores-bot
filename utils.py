def flex_today_matches_builder(home_team, away_team, home_goals, away_goals, time, home_code, away_code):
    teams_pict_url = {
        'RUS': 'https://upload.wikimedia.org/wikipedia/commons/f/f3/Flag_of_Russia.svg',
        'KSA': 'https://upload.wikimedia.org/wikipedia/commons/0/0d/Flag_of_Saudi_Arabia.svg',
        'EGY': 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Egypt.svg',
        'URU': 'https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Uruguay.svg',
        'MAR': 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Morocco.svg',
        'IRN': 'https://upload.wikimedia.org/wikipedia/commons/c/ca/Flag_of_Iran.svg',
        'POR': 'https://upload.wikimedia.org/wikipedia/commons/5/5c/Flag_of_Portugal.svg',
        'ESP': 'https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Spain.svg',
        'FRA': 'https://upload.wikimedia.org/wikipedia/commons/c/c3/Flag_of_France.svg',
        'AUS': 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Flag_of_Australia.svg',
        'ARG': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/Flag_of_Argentina.svg',
        'ISL': 'https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Iceland.svg',
        'PER': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Flag_of_Peru.svg',
        'DEN': 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Flag_of_Denmark.svg',
        'CRO': 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Flag_of_Croatia.svg',
        'NGA': 'https://upload.wikimedia.org/wikipedia/commons/7/79/Flag_of_Nigeria.svg',
        'CRC': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Flag_of_Costa_Rica_(state).svg', 
        'SRB': 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Flag_of_Serbia.svg', 
        'GER': 'https://upload.wikimedia.org/wikipedia/commons/b/ba/Flag_of_Germany.svg', 
        'MEX': 'https://upload.wikimedia.org/wikipedia/commons/f/fc/Flag_of_Mexico.svg', 
        'BRA': 'https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg', 
        'SUI': 'https://upload.wikimedia.org/wikipedia/commons/0/08/Flag_of_Switzerland_(Pantone).svg', 
        'SWE': 'https://upload.wikimedia.org/wikipedia/commons/4/4c/Flag_of_Sweden.svg', 
        'KOR': 'https://upload.wikimedia.org/wikipedia/commons/0/09/Flag_of_South_Korea.svg', 
        'BEL': 'https://upload.wikimedia.org/wikipedia/commons/9/92/Flag_of_Belgium_(civil).svg', 
        'PAN': 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Flag_of_Panama.svg', 
        'TUN': 'https://upload.wikimedia.org/wikipedia/commons/c/ce/Flag_of_Tunisia.svg',
        'ENG': 'https://upload.wikimedia.org/wikipedia/commons/b/be/Flag_of_England.svg', 
        'COL': 'https://upload.wikimedia.org/wikipedia/commons/2/21/Flag_of_Colombia.svg',
        'JPN': 'https://upload.wikimedia.org/wikipedia/commons/9/9e/Flag_of_Japan.svg', 
        'POL': 'https://upload.wikimedia.org/wikipedia/commons/1/12/Flag_of_Poland.svg', 
        'SEN': 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Flag_of_Senegal.svg'}
    
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
                                "url": teams_pict_url[home_code]
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
                                "url": teams_pict_url[away_code]
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
