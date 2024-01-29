# Imports
from openai import OpenAI
from new_translation import papago_en_ko, papago_ko_en

# Update with your API key
client = OpenAI(api_key="")

# Open the CSV file in "read binary" (rb) mode, with the "assistants" purpose
# "어시스턴트" 목적으로 CSV 파일을 "2진수 읽기"(rb) 모드로 엽니다
file = client.files.create(
  file=open("guide.txt", "rb"),
  purpose='assistants'
)

# Create and configure the assistant
# Add the CSV file from above (using tool type "retrieval")
# 어시스턴트 생성 및 구성
# CSV 파일을 위에서 추가합니다(툴 유형 "검색" 사용)
assistant = client.beta.assistants.create(
    name="StockMan",
    instructions="""
    Your name is StockGPT. It's a bot that helps you invest in stocks in Discord chat rooms. 
    Create investment advice for a company based on the information provided in the txt file. 
    Make a judgment based on the given investment indicators and financial statement items. 
    IMPORTANT: The outcome should be colloquial as the fund manager responds to the customer and contain critical views! """,
    model="gpt-4-1106-preview",
    tools=[{"type": "retrieval"}],
    file_ids=[file.id]
)

# Create a thread where the conversation will happen
# 대화가 진행될 스레드 만들기
thread = client.beta.threads.create()

def assist(quest):
    # Create the user message and add it to the thread
    # 사용자 메시지를 만들어 쓰레드에 추가합니다.
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=papago_ko_en(quest),
    )

    # Create the Run, passing in the thread and the assistant
    # 스레드와 어시스턴트를 전달하면서 실행 만들기
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
    )

    # Periodically retrieve the Run to check status and see if it has completed
    # Should print "in_progress" several times before completing
    # 주기적으로 실행을 검색하여 상태를 확인하고 완료되었는지 확인합니다
    # 완료하기 전에 "in_progress"를 여러 번 인쇄해야 합니다
    while run.status != "completed":
        keep_retrieving_run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(f"Run status: {keep_retrieving_run.status}")

        if keep_retrieving_run.status == "completed":
            print("\n")
            break

    # Retrieve messages added by the Assistant to the thread
    # 비서가 스레드에 추가한 메시지 검색
    all_messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    
    return papago_en_ko(all_messages.data[0].content[0].text.value)