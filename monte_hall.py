import random

def monty_hall_simulation(num_trials):
    
    for _ in range(num_trials):

    # 참가자가 선택을 변경
        remaining_door = doors[0] if choice == doors.index(doors[1]) else doors[1]

        # 결과 계산
        if doors[choice] == 'car':
            stay_wins += 1
        elif remaining_door == 'car':
            switch_wins += 1

    # 결과 출력
    print(f"Staying wins: {stay_wins} ({(stay_wins / num_trials) * 100:.2f}%)")
    print(f"Switching wins: {switch_wins} ({(switch_wins / num_trials) * 100:.2f}%)")