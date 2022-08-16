menu = [
    {
        'name': 'menu1',
        'keyboards': [
            {
                'buttons': [
                    {
                        'text': 'Открыть меню',
                        'status': 1
                    }
                ],
                'handler': 'otkr_menu'
            }
        ],
        'type': 'row'
    },
    {
        'name': 'menu2',
        'keyboards': [
            {
                'buttons': [
                    {
                        'text': 'Открыть меню',
                        'status': 1
                    }
                ],
                'handler': 'otkr_menu'
            },
            {
                'buttons': [
                    {
                        'text': 'Вывести файл',
                        'status': 1
                    }
                ],
                'handler': 'file_excel_loader',
                'status': 1
            },
        ],
        'type': 'row'
    },
    {
        'name': 'menu3',
        'keyboards': [
            {
                'buttons': [
                    {
                        'text': 'Где найти нужный тур?',
                        'status': 1
                    }
                ],
                'handler': 'maps'
            },
            {
                'buttons': [
                    {
                        'text': 'СOЧИ',
                        'status': 1
                    }
                ],
                'handler': 'sochy'
            },
            {
                'buttons': [
                    {
                        'text': 'АБХАЗИЯ',
                        'status': 1
                    }
                ],
                'handler': 'abhaz'
            },
            {
                'buttons': [
                    {
                        'text': 'МОРЕ',
                        'status': 1
                    }
                ],
                'handler': 'voda'
            },
            {
                'buttons': [
                    {
                        'text': 'АКТИВ',
                        'status': 1
                    }
                ],
                'handler': 'vozduh'
            },
        ],
        'type': 'row'
    },
    # sochi
    {
        'name': 'sochi',
        'keyboards': [
            {
                'buttons': [
                    {
                        'text': 'Красная Поляна',
                        'status': 1
                    },
                    {
                        'text': 'Обзорная Сочи',
                        'status': 1
                    },
                    {
                        'text': '33 Водопада',
                        'status': 1
                    },
                    {
                        'text': 'Воронцовские пещеры',
                        'status': 1
                    },
                    {
                        'text': 'Каньоны Псахо (джип-тур)',
                        'status': 1
                    },
                    {
                        'text': 'Мамонтово Ущелье (джип-тур)',
                        'status': 1
                    },
                    {
                        'text': 'Эпоха времени',
                        'status': 1
                    },
                ],
                'handler': 'dat_ukaz'
            }
        ],
        'type': 'row'
    },
    # abkhazia
    {
        'name': 'abkhazia',
        'keyboards': [
            {
                'buttons': [
                    {
                        'text': 'Золотое Кольцо',
                        'status': 1
                    },
                    {
                        'text': 'Абхазское застолье',
                        'status': 1
                    },
                    {
                        'text': 'Термальные Источники',
                        'status': 1
                    },
                    {
                        'text': 'Абхазский драйв (джип-тур)',
                        'status': 1
                    },
                ],
                'handler': 'dat_ukaz'
            }
        ],
        'type': 'row'
    },
    # more
    {
        'name': 'more',
        'keyboards': [
            {
                'buttons': [
                    {
                        'text': 'Морская прогулка',
                        'status': 1
                    },
                    {
                        'text': 'Рыбалка в море',
                        'status': 1
                    },
                    {
                        'text': 'АРЕНДА ЯХТ',
                        'status': 1
                    }
                ],
                'handler': 'dat_ukaz'
            }
        ],
        'type': 'row'
    },
    # activ
    {
        'name': 'activ',
        'keyboards': [
            {
                'buttons': [
                    {
                        'text': 'Рафтинг',
                        'status': 1
                    },
                    {
                        'text': 'Квадроциклы',
                        'status': 1
                    },
                    {
                        'text': 'Конные Прогулки',
                        'status': 1
                    },
                    {
                        'text': 'Солохаул (джип-тур)',
                        'status': 1
                    },
                    {
                        'text': 'Дайвинг',
                        'status': 1
                    },
                    {
                        'text': 'Параплан',
                        'status': 1
                    },
                ],
                'handler': 'dat_ukaz'
            }
        ],
        'type': 'row'
    }
]
