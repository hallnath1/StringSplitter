import re


class TagManipulator():
    def parse_string(self, tags, regex=""):
        result = []
        tempResult = re.split(regex, tags)

        for i, tag in enumerate(tempResult):
            if tag != "":
                result.append(tag.lstrip())

        return result
