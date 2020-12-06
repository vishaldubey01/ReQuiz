/* eslint-disable react/no-array-index-key */
import { useState, useEffect } from "react";
import MCQButton from "./MCQButton";

const MCQ = ({
  id,
  selected,
  setSelected,
  nextQuestion,
  answerIndex,
  previousQuestion,
  currentQuestion,
}) => {
  const [correct, setCorrect] = useState(undefined);
  const [disable, setDisable] = useState(false);
  var sprint = require("../data/questions.json");

  // Set state to empty each time the component refreshes
  // It runs every time the prop "selected" is updated
  useEffect(() => {
    setCorrect(undefined);
    setDisable(false);
    console.log(data);
  }, [selected]);

  // Function to send a POST request to check the answer
  const checkAnswer = async (answer) => {
    if (value.correct) {
      showCorrectModal();
    } else {
      showIncorrectModal();
    }

    setDisable(true); // Disable current question
  };

  // Simple change handler to change which option is selected
  const handleChange = (e) => {
    setSelected(e.target.value);
  };

  // Handle form submit
  const handleFormSubmit = (e) => {
    e.preventDefault();
    checkAnswer(selected);
  };

  const showCorrectModal = () => {
    setCorrect("correct");
    // alert("Correct answer");
  };

  const showIncorrectModal = () => {
    setCorrect("incorrect");
    // alert("Incorrect answer");
  };

  return (
    <div className="container">
      <div>
        <section className="question">
          <h3>Question {sprint[currentQuestion].id}</h3>
          <p>sprint</p>
        </section>
        <aside>
          <div className="flex-row flex justify-evenly">
            {currentQuestion > 0 && (
              <button
                type="button"
                onClick={previousQuestion}
                className=" arrow left noHover my-auto mx-0"
                aria-label="Previous"
              />
            )}
            <h4>Answers</h4>
            <button
              type="button"
              onClick={nextQuestion}
              className=" arrow right noHover my-auto mx-0"
              aria-label="Next"
            />
          </div>
          <form onSubmit={handleFormSubmit}>
            {JSON.parse(sprint[currentQuestion].content).answers.map(
              (answer, index) => {
                let correct1 = "default";
                // console.log("selected", selected);
                if (correct) {
                  if (index === answerIndex) {
                    correct1 = "correct";
                  } else {
                    correct1 = "incorrect";
                  }
                }
                return (
                  <MCQButton
                    id={index}
                    key={index}
                    name="answer"
                    value={index}
                    checked={Number(selected) === index}
                    onChange={handleChange}
                    correct={correct1}
                    disabled={disable}
                  >
                    {/* <MathJax math={answer} /> */}
                  </MCQButton>
                );
              }
            )}
            <br />

            {!correct ? (
              <button
                type="submit"
                className="w-full block text-white bg-blue-500 max-w-md my-4 font-medium mx-auto rounded-full h-10 uppercase leading-relaxed"
                disabled={selected === -1}
              >
                Check answer
              </button>
            ) : (
              <button
                type="button"
                onClick={nextQuestion}
                className={`${
                  correct === "correct" ? "bg-success" : "bg-failure"
                } w-full block text-white max-w-md my-4 font-medium mx-auto rounded-full h-10 uppercase leading-relaxed`}
              >
                Next question
              </button>
            )}
          </form>
        </aside>

        <section>
          <ul className={`${disable ? "block" : "hidden"}`}>
            {JSON.parse(sprint[currentQuestion].content).guidance &&
              JSON.parse(sprint[currentQuestion].content).guidance.map(
                (current, index) => {
                  return (
                    <li className="border-green-200 bg-green-200 my-4 rounded-md px-2 py-2">
                      <span className="bg-white rounded-full float-left h-8 w-8 flex items-center justify-center mx-4 text-gray-700">
                        {index}
                      </span>
                      <span>
                        {current.map((text) => {
                          //   return <MathJax math={text.content} />;
                        })}
                      </span>
                    </li>
                  );
                }
              )}
          </ul>
        </section>
      </div>

      <style jsx>{`
        .arrow {
          border: solid grey;
          border-width: 0 3px 3px 0;
          display: inline-block;
          padding: 3px;
          height: 10px;
          width: 10px;
          outline: none;
        }

        button:hover {
          outline: none;
        }

        .right {
          transform: rotate(-45deg);
          -webkit-transform: rotate(-45deg);
        }

        .left {
          transform: rotate(135deg);
          -webkit-transform: rotate(135deg);
        }
        .container {
          overflow: hidden;
          margin: 0 auto;
        }

        .container > * {
          display: flex;
          flex-wrap: wrap;
          margin: calc(20px / 2 * -1);
        }

        .container > * > * {
          margin: calc(20px / 2);
          flex-grow: 1;
        }

        .question {
          max-width: 70%;
        }

        .container > * > :first-child {
          flex-basis: 0;
          flex-grow: 999;
          min-width: calc(60% - 20px);
        }
      `}</style>
    </div>
  );
};

export default MCQ;
