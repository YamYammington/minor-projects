from datetime import datetime
import sys


def readable_timestamp(time: datetime | int | float) -> str:
    if isinstance(time, int) or isinstance(time, float):
        time = datetime.fromtimestamp(time)
    now = datetime.now()
    delta = now - time
    if (delta.seconds * -1) > delta.seconds:  # check if in future
        return "somewhere in the future"
    if delta.days == 0:
        if delta.seconds < 60:
            return f"{delta.seconds} seconds ago"
        elif delta.seconds < 120:
            return "1 minute ago"
        elif delta.seconds < 3600:
            return f"{delta.seconds // 60} minutes ago"
        elif delta.seconds < 7200:
            return "1 hour ago"
        elif delta.seconds < 86400:
            return f"{delta.seconds // 3600} hours ago"
    elif delta.days == 1:
        return "yesterday"
    elif delta.days < 7:
        return f"{delta.days} days ago"
    elif delta.days < 31:
        return f"{delta.days // 7} weeks ago"
    elif delta.days < 365:
        return f"{delta.days // 30} months ago"
    else:
        return f"{delta.days // 365} years ago"


if __name__ == "__main__":
    epoch = int(sys.argv[1]) if len(sys.argv) > 1 else input("Epoch to convert: ")

    result = readable_timestamp(epoch)
    print(result)
