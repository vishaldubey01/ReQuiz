import DashboardTemplate from "../components/DashboardTemplate";
import Question from "../components/Question";

export default function Quiz() {
  return (
    <DashboardTemplate>
      <div className="max-w-7xl mx-auto">
        <h1 className="text-2xl font-semibold text-gray-900">Quizzes</h1>
      </div>
      <div>
        <Question />
      </div>
    </DashboardTemplate>
  );
}
