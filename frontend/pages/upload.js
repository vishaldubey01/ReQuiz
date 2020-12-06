import { useState } from "react";
import DashboardTemplate from "../components/DashboardTemplate";

export default function Dashboard() {
  const [title, setTitle] = useState("");
  return (
    <DashboardTemplate>
      <h1>Upload files here</h1>
      <form>
        <div>
          <label
            htmlFor="title"
            class="block text-sm font-medium text-gray-700"
          >
            Title
          </label>
          <div class="mt-1 relative rounded-md shadow-sm">
            <input
              type="text"
              onChange={(e) => setTitle(e.target.value)}
              name="title"
              id="title"
              className="focus:ring-indigo-500 focus:border-indigo-500 block w-1/3 sm:text-sm border-gray-300 rounded-md"
              placeholder="Title"
            />
          </div>
        </div>
        <textarea
          className="focus:ring-indigo-500 focus:border-indigo-500 block w-1/3 sm:text-sm border-gray-300 rounded-md"
          id="upload-text"
          name="w3review"
          rows="4"
          cols="45"
        >
          Upload any text here to generate a quiz from it
        </textarea>
        <button
          type="submit"
          className="mt-4 flex items-center px-6 py-3 border border-transparent shadow-sm text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Upload text
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
            />
          </svg>
        </button>
      </form>
    </DashboardTemplate>
  );
}
