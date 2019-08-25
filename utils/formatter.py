import json
from pathlib import Path


class Formatter:

    def __call__(self, lang="en", f_type="npc", **kwargs):

        if f_type == "npc":
            self.__format_npc_names(lang)
        elif f_type == "quest":
            with open(Path(__file__).parent / "../output/{}_quest_data.json".format(lang), "r", encoding="utf-8") as f:
                quest_input = json.load(f)
                quest_input.sort(key=lambda k: k["id"])

            with open(Path(__file__).parent / "../output/{}.lua".format(lang), "a", encoding="utf-8") as g:
                g.write("\nLangQuestLookup = {\n")

                for item in quest_input:
                    title = item["title"]
                    title = title.replace("'", "\\'")

                    objective = item["objective"]
                    objective = objective.replace("'", "\\'")

                    description = item["description"]
                    description = description.replace("'", "\\'")

                    g.write("\t[{id}] = {{'{title}', '{desc}', '{obj}'}},\n".format(id=item["id"], title=title,
                                                                                    desc=description, obj=objective))

                g.write("}")

    @staticmethod
    def __format_npc_names(lang):
        with open(Path(__file__).parent / "../output/{}_npc_data.json".format(lang), "r", encoding="utf-8") as f:
            npc_input = json.load(f)
            npc_input.sort(key=lambda k: int(k["id"]))
        with open(Path(__file__).parent / "../output/{}.lua".format(lang), "a", encoding="utf-8") as g:
            g.write("\nLangNameLookup = {\n")

            for item in npc_input:
                name = item["name"]
                name = name.replace("'", "\\'")
                g.write("\t[{}] = '{}',\n".format(item["id"], name))

            g.write("}")


if __name__ == '__main__':
    f = Formatter()
    f("fr", "quest")
