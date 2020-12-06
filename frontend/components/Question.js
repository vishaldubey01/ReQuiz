import { useState } from "react";
import MCQButton from "./MCQButton";

export default function Question() {
  const [correct, setCorrect] = useState(undefined);
  const [disable, setDisable] = useState(false);
  const [selected, setSelected] = useState(-1);
  var sprint = require("../data/questions.json");

  // Function to send a POST request to check the answer
  const checkAnswer = async () => {
    sprint[0].answer.map((answer, index) => {
      if (index === selected) {
        showCorrectModal();
      } else {
        showIncorrectModal();
      }
    });

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
    <div>
      <h1>{sprint[0].question}</h1>
      <form onSubmit={handleFormSubmit}>
        {sprint[0].answer.map((answer, index) => {
          let correct1 = "default";
          // console.log("selected", selected);
          if (correct) {
            if (index === 0) {
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
              {answer.answer}
            </MCQButton>
          );
        })}
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
            // onClick={nextQuestion}
            className={`${
              correct === "correct" ? "bg-green-500" : "bg-red-500"
            } w-full block text-white max-w-md my-4 font-medium mx-auto rounded-full h-10 uppercase leading-relaxed`}
          >
            Next question
          </button>
        )}
      </form>
    </div>
  );
}
