starter_title = '<h1 style="color: rgb(90, 184, 214)"><b>Validador de site</b></h1>'
safe_title = '<h1 style="color: rgb(92, 211, 125)"><b>Validador de site</b></h1>'
warning_title = '<h1 style="color: rgb(251, 185, 0)"><b>Validador de site</b></h1>'
dangerous_title = '<h1 style="color: rgb(255, 103, 103)"><b>Validador de site</b></h1>'

safe_body = """<!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f9f9f9;
                    }
                    .container {
                    text-align: center;
                    }
                    .status {
                    background-color: rgb(92, 211, 125);
                    color: white;
                    padding: 10px 20px;
                    border-radius: 8px;
                    font-size: 20px;
                    margin: 10px 0;
                    }
                    .description {
                    color: #999999;
                    font-size: 14px;
                    }
                </style>
                </head>
                <body>
                <div class="container">
                    <div class="status">Site Seguro</div>
                    <div class="description">O site foi validado e pode ser acessado sem riscos à segurança</div>
                </div>
                </body>
                </html>
"""
warning_body = """<!DOCTYPE html>
                    <html lang="pt-BR">
                    <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <style>
                        body {
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background-color: #f9f9f9;
                        }
                        .container {
                        text-align: center;
                        }
                        .status {
                        background-color: #FFB100;
                        color: white;
                        padding: 10px 20px;
                        border-radius: 8px;
                        font-size: 20px;
                        margin: 10px 0;
                        }
                        .description {
                        color: #999999;
                        font-size: 14px;
                        }
                    </style>
                    </head>
                    <body>
                    <div class="container">
                        <div class="status">Site Duvidoso</div>
                        <div class="description">O site foi avaliado e pode ser acessado com cautela, pois pode oferecer riscos à segurança</div>
                    </div>
                    </body>
                    </html>
"""
dangerous_body = """<!DOCTYPE html>
                        <html lang="pt-BR">
                        <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <style>
                            body {
                            font-family: Arial, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                            background-color: #f9f9f9;
                            }
                            .container {
                            text-align: center;
                            }
                            .status {
                            background-color: #FF6B6B;
                            color: white;
                            padding: 10px 20px;
                            border-radius: 8px;
                            font-size: 20px;
                            margin: 10px 0;
                            }
                            .description {
                            color: #999999;
                            font-size: 14px;
                            }
                        </style>
                        </head>
                        <body>
                        <div class="container">
                            <div class="status">Site Perigoso</div>
                            <div class="description">O site foi avaliado e não deve ser acessado por apresentar riscos altíssimos à segurança</div>
                        </div>
                        </body>
                        </html>
"""
