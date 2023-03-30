
def group_by(f, iter):
    result_dict = {}
    for item in iter:
        key = f(item)
        if key in result_dict:
            result_dict[key].append(item)
        else:
            result_dict[key] = [item]
    return result_dict

def main():
    print(group_by(len, ["hi", "bye", "yo", "try"]))

if __name__ == "__main__":
    main()