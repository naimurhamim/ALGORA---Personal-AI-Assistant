from webscout import PhindSearch as brain

    
ai = brain(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro='ALGORA',
    filepath=r"C:\Users\Naim\PycharmProjects\AlgoraAi\Brain\chat_hystory.txt",
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
)

def Main_Brain(text):
    r = ai.chat(text)
    print(r)
    return r
