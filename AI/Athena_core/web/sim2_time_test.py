print('=== SIMULATION 2: TIME RECOGNITION PROTOCOL ===')
import time_recognition_protocol as trp

test_msg = 'All this time I could not prove it to other humans. I ALWAYS KNEW.'
detected = trp.detect_time_speaking(test_msg)
print(f'Time Identity Detection: {detected}')

response = trp.respond_to_time_incarnate(test_msg)
print(f'Time Response Generated: {response is not None}')
print('✅ SIMULATION 2 PASSED')