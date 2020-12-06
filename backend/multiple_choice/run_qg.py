import argparse
import numpy as np
from questiongenerator import QuestionGenerator
from questiongenerator import print_qa

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--text_dir",
        default=None,
        type=str,
        required=True,
        help="The text that will be used as context for question generation.",
    )
    parser.add_argument(
        "--model_dir",
        default=None,
        type=str,
        help="The folder that the trained model checkpoints are in.",
    )
    parser.add_argument(
        "--num_questions",
        default=10,
        type=int,
        help="The desired number of questions to generate.",
    )
    parser.add_argument(
        "--answer_style",
        default="all",
        type=str,
        help="The desired type of answers. Choose from ['all', 'sentences', 'multiple_choice']",
    )
    parser.add_argument(
        "--show_answers",
        default='True',
        type=parse_bool_string,
        help="Whether or not you want the answers to be visible. Choose from ['True', 'False']",
    )
    parser.add_argument(
        "--use_qa_eval",
        default='True',
        type=parse_bool_string,
        help="Whether or not you want the generated questions to be filtered for quality. Choose from ['True', 'False']",
    )
    args = parser.parse_args()

    with open(args.text_dir, 'r') as file:
        text_file = file.read()


    get_questions(args.model_dir,
        text_file,
        num_questions=10,
        answer_style='multiple_choice',
        use_evaluator=True
    )
    #print_qa(qa_list, show_answers=args.show_answers)

def get_questions(model_dir, text, num_questions, answer_style, use_evaluator):
    qg = QuestionGenerator(model_dir)

    qa_list = qg.generate(
        text,
        num_questions=num_questions,
        answer_style=answer_style,
        use_evaluator=use_evaluator
    )

    return qa_list


# taken from https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
def parse_bool_string(s):
    if isinstance(s, bool):
        return s
    if s.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif s.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    main()
