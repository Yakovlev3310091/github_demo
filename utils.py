import json

def get_candidates(url):
    with open(url, 'r', encoding='utf-8') as candidates:  # открывает файл для чтения
        return json.load(candidates)

def format_candidates(candidates_list):
    result = "<pre>"
    for candidate in candidates_list:  # проходя по всем ключам
        result += (
            f" Имя кандидата - {candidate['name']}\n"  # запись имени в список   
            f" Позиция кандидата - {candidate['position']}\n"  # запись позиции в список
            f" Навыки через запятую - {candidate['skills']}\n\n"  # запись навыков в список
        )
    result += "<pre>"
    return result

def get_candidate_by_id(candidates_list, candidate_id):
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_skill(candidates_list, candidate_skill):
    result = []

    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)
    return result
