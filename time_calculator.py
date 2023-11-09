
def add_time(start, duration, start_day=None):

  week_days = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
  new_day = ''
  
  start_time_parts = start.split()
  start_time = start_time_parts[0]
  meridem = start_time_parts[1]
  
  start_hours, start_minute = map(int, start_time.split(':'))
  duration_hours, duration_minutes = map(int, duration.split(':'))
  
  if (meridem == 'PM'):
    start_hours += 12

  total_minutes = start_minute + duration_minutes
  total_hours = start_hours + duration_hours
  
  if (total_minutes >= 60):
    total_minutes -= 60
    total_hours += 1
    
  next_day = total_hours // 24
  total_hours %= 24

  if (total_hours >= 12):
    meridem = 'PM'
    if (total_hours > 12):
      total_hours -= 12
  else:
    meridem = 'AM'
    if (total_hours == 0):
      total_hours = 12

  if (start_day):
    start_day = start_day.lower()
    if (start_day in week_days):
      num_day = week_days[start_day]
      end_day = (next_day + num_day) % 7
      new_day = list(week_days.keys())[list(week_days.values()).index(end_day)].capitalize()

  formatted_time = f"{total_hours}:{total_minutes:02d} {meridem}"

  if (new_day):
    formatted_time += f", {new_day}"

  if (next_day == 1):
    formatted_time += " (next day)"
  elif (next_day > 1):
    formatted_time += f" ({next_day} days later)"

  return formatted_time