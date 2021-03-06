import { useState } from "react";
import DashboardTemplate from "../components/DashboardTemplate";

export default function Dashboard() {
  const [title, setTitle] = useState("");
  const [text, setText] = useState("");

  return (
    <DashboardTemplate>
      <div className="max-w-7xl mx-auto">
        <h1 className="text-2xl font-semibold text-gray-900">Upload</h1>
      </div>
      <form>
        <div>
          <label
            htmlFor="title"
            className="block text-sm font-medium text-gray-700"
          >
            Title
          </label>
          <div className="w-1/3 mt-1 relative rounded-md shadow-sm">
            <input
              type="text"
              onChange={(e) => setTitle(e.target.value)}
              name="title"
              id="title"
              value={title}
              className="focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
              placeholder="Title"
            />
          </div>
        </div>
        <br />
        <div>
          <label
            htmlFor="upload-text"
            className="block text-sm font-medium text-gray-700"
          >
            Upload text
          </label>
          <div className="w-1/3 mt-1 relative rounded-md shadow-sm">
            <textarea
              className="focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
              id="upload-text"
              name="upload-text"
              rows="4"
              cols="45"
              placeholder="Upload any text here to generate a quiz from it"
              value={text}
              onChange={(e) => setText(e.target.value)}
            ></textarea>
          </div>
        </div>
        <button
          type="submit"
          className="mt-4 flex items-center px-6 py-3 border border-transparent shadow-sm text-base font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Upload text
          <svg
            className="ml-2 h-6 w-6"
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
