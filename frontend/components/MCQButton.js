// src/components/MCQButton.jsx

const MCQButton = ({
  id,
  value,
  name,
  children,
  onChange,
  checked,
  correct,
  disabled,
}) => {
  return (
    <>
      <label className="radio" htmlFor={id}>
        <input
          type="radio"
          name={name}
          id={id}
          value={value}
          onChange={onChange}
          checked={checked}
          correct={correct}
          disabled={disabled}
        />
        <span>{children}</span>
      </label>
      <style jsx>{`
        label {
          display: block;
          cursor: pointer;
          text-align: center;
          margin: 1em 0;
          min-width: 200px;
        }
        label input {
          position: absolute;
          top: 0;
          left: 0;
          visibility: hidden;
          pointer-events: none;
        }
        label span {
          padding: 7px 14px;
          border: 2px solid #eee;
          display: block;
          border-radius: 3px;
        }
        label input:checked[correct="default"] + span {
          border-color: blue;
        }
        label input[correct="correct"] + span {
          border-color: green;
        }
        label input:checked[correct="incorrect"] + span {
          border-color: red;
        }
        label input:disabled + span {
          cursor: not-allowed;
        }
      `}</style>
    </>
  );
};

export default MCQButton;
