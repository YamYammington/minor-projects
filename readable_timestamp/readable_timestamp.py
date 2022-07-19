from datetime import datetime
import sys


def readable_timestamp(t: datetime | int | float) -> str:
    """
    :param t: epoch timestamp (either integer or floating point) or datetime object
    :return: human-readable time

    Converts a timestamp to a human-readable time, such as: "1 hour ago" or "2 days ago"
    """
    if isinstance(t, int) or isinstance(t, float):
        t = datetime.fromtimestamp(t)
    now = datetime.now()
    delta = now - t
    if (delta.seconds * -1) > delta.seconds:  # check if in future
        return "Somewhere in the future"
    if delta.days == 0:
        if delta.seconds < 60:
            return "just now"
        elif delta.seconds < 120:
            return "1 minute ago"
        elif delta.seconds < 3600:
            return str(delta.seconds // 60) + " minutes ago"
        elif delta.seconds < 7200:
            return "1 hour ago"
        elif delta.seconds < 86400:
            return str(delta.seconds // 3600) + " hours ago"
    elif delta.days == 1:
        return "Yesterday"
    elif delta.days < 7:
        return str(delta.days) + " days ago"
    elif delta.days < 31:
        return str(delta.days // 7) + " weeks ago"
    elif delta.days < 365:
        return str(delta.days // 30) + " months ago"
    else:
        return str(delta.days // 365) + " years ago"


if __name__ == "__main__":
    epoch = int(sys.argv[1]) if len(sys.argv) > 1 else input("Epoch to convert: ")

    result = readable_timestamp(epoch)
    print(result)
