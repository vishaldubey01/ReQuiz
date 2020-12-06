import { useState } from "react";
import Footer from "../components/footer";
import Navbar from "../components/Navbar";
import Link from "next/link";
import { useRouter } from "next/router";

export default function DashboardTemplate({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const router = useRouter();

  return (
    <div>
      <main className="">
        <div className="h-screen flex overflow-hidden bg-gray-100">
          {/* Off-canvas menu for mobile, show/hide based on off-canvas menu state. */}
          {sidebarOpen && (
            <div className="md:hidden">
              <div className="fixed inset-0 flex z-40">
                <div className="fixed inset-0" aria-hidden="true">
                  <div className="absolute inset-0 bg-gray-600 opacity-75"></div>
                </div>

                <div className="relative flex-1 flex flex-col max-w-xs w-full pt-5 pb-4 bg-gray-800">
                  <div className="absolute top-0 right-0 -mr-12 pt-2">
                    <button
                      onClick={() => setSidebarOpen(false)}
                      className="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                    >
                      <span className="sr-only">Close sidebar</span>

                      <svg
                        className="h-6 w-6 text-white"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M6 18L18 6M6 6l12 12"
                        />
                      </svg>
                    </button>
                  </div>
                  <div className="flex-shrink-0 flex items-center px-4">
                    <img
                      className="h-8 w-auto"
                      src="./logo.png"
                      alt="Workflow"
                    />
                  </div>
                  <div className="mt-5 flex-1 h-0 overflow-y-auto">
                    <nav className="px-2 space-y-1">
                      {/* Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" */}
                      <a
                        href="#"
                        className="bg-gray-900 text-white group flex items-center px-2 py-2 text-base font-medium rounded-md"
                      >
                        {/* Current: "text-gray-300", Default: "text-gray-400 group-hover:text-gray-300" */}
                        {/* Heroicon name: home */}
                        <svg
                          className="text-gray-300 mr-4 h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                          />
                        </svg>
                        Dashboard
                      </a>

                      <a
                        href="#"
                        className="text-gray-300 hover:bg-gray-700 hover:text-white group flex items-center px-2 py-2 text-base font-medium rounded-md"
                      >
                        {/* Heroicon name: users */}
                        <svg
                          className="text-gray-400 group-hover:text-gray-300 mr-4 h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                          />
                        </svg>
                        Profile
                      </a>

                      <Link href="/upload">
                        <a
                          className={`${
                            router.pathname == "/upload"
                              ? "bg-gray-900 text-white"
                              : "text-gray-300 hover:bg-gray-700 hover:text-white"
                          } group flex items-center px-2 py-2 text-base font-medium rounded-md`}
                        >
                          {/* Heroicon name: folder */}
                          <svg
                            className={`${
                              router.pathname == "/upload"
                                ? "text-gray-300"
                                : "text-gray-400 group-hover:text-gray-300"
                            }}  mr-4 h-6 w-6`}
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                            aria-hidden="true"
                          >
                            <path
                              strokeLinecap="round"
                              strokeLinejoin="round"
                              strokeWidth="2"
                              d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"
                            />
                          </svg>
                          Upload
                        </a>
                      </Link>

                      <a
                        href="#"
                        className="text-gray-300 hover:bg-gray-700 hover:text-white group flex items-center px-2 py-2 text-base font-medium rounded-md"
                      >
                        {/* Heroicon name: calendar */}
                        <svg
                          className="text-gray-400 group-hover:text-gray-300 mr-4 h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                          />
                        </svg>
                        Calendar
                      </a>

                      <a
                        href="#"
                        className="text-gray-300 hover:bg-gray-700 hover:text-white group flex items-center px-2 py-2 text-base font-medium rounded-md"
                      >
                        {/* Heroicon name: inbox */}
                        <svg
                          className="text-gray-400 group-hover:text-gray-300 mr-4 h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
                          />
                        </svg>
                        Quizzes
                      </a>

                      <a
                        href="#"
                        className="text-gray-300 hover:bg-gray-700 hover:text-white group flex items-center px-2 py-2 text-base font-medium rounded-md"
                      >
                        {/* Heroicon name: chart-bar */}
                        <svg
                          className="text-gray-400 group-hover:text-gray-300 mr-4 h-6 w-6"
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                          />
                        </svg>
                        Reports
                      </a>
                    </nav>
                  </div>
                </div>

                <div className="flex-shrink-0 w-14" aria-hidden="true">
                  {/* Dummy element to force sidebar to shrink to fit close icon */}
                </div>
              </div>
            </div>
          )}

          {/* Static sidebar for desktop */}
          <div className="hidden md:flex md:flex-shrink-0">
            <div className="flex flex-col w-64">
              {/* Sidebar component, swap this element with another sidebar if you like */}
              <div className="flex flex-col h-0 flex-1">
                <div className="flex items-center h-16 flex-shrink-0 px-4 bg-gray-900 justify-center">
                  <img
                    className="h-16 w-auto"
                    src="./logo.png"
                    alt="Workflow"
                  />
                </div>
                <div className="flex-1 flex flex-col overflow-y-auto">
                  <nav className="flex-1 px-2 py-4 bg-gray-800 space-y-1">
                    {/* Current: "bg-gray-200 text-gray-900", Default: "text-gray-600 hover:bg-gray-50 hover:text-gray-900" */}
                    <Link href="/dashboard">
                      <a
                        className={`${
                          router.pathname == "/dashboard"
                            ? "bg-gray-200 text-gray-900"
                            : "text-gray-300 hover:bg-gray-700 hover:text-white"
                        } text-white group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
                      >
                        {/* Current: "text-gray-300", Default: "text-gray-400 group-hover:text-gray-300" */}
                        {/* Heroicon name: home */}
                        <svg
                          className={`${
                            router.pathname == "/dashboard"
                              ? "text-gray-700"
                              : "text-gray-400 group-hover:text-gray-300"
                          } text-gray-300 mr-3 h-6 w-6`}
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"
                          />
                        </svg>
                        Dashboard
                      </a>
                    </Link>

                    <Link href="/profile">
                      <a
                        className={`${
                          router.pathname == "/profile"
                            ? "bg-gray-200 text-gray-900"
                            : "text-gray-300 hover:bg-gray-700 hover:text-white"
                        } text-white group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
                      >
                        {/* Heroicon name: users */}
                        <svg
                          className={`${
                            router.pathname == "/profile"
                              ? "text-gray-700"
                              : "text-gray-400 group-hover:text-gray-300"
                          } text-gray-300 mr-3 h-6 w-6`}
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                          />
                        </svg>
                        Profile
                      </a>
                    </Link>

                    <Link href="/upload">
                      <a
                        className={`${
                          router.pathname == "/upload"
                            ? "bg-gray-200 text-gray-900"
                            : "text-gray-300 hover:bg-gray-700 hover:text-white"
                        } group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
                      >
                        {/* Heroicon name: folder */}
                        <svg
                          className={`${
                            router.pathname == "/upload"
                              ? "text-gray-700"
                              : "text-gray-400 group-hover:text-gray-300"
                          } text-gray-300 mr-3 h-6 w-6`}
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z"
                          />
                        </svg>
                        Upload
                      </a>
                    </Link>

                    <Link href="/quiz">
                      <a
                        className={`${
                          router.pathname == "/quiz"
                            ? "bg-gray-200 text-gray-900"
                            : "text-gray-300 hover:bg-gray-700 hover:text-white"
                        } group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
                      >
                        {/* Heroicon name: inbox */}
                        <svg
                          className={`${
                            router.pathname == "/quiz"
                              ? "text-gray-700"
                              : "text-gray-400 group-hover:text-gray-300"
                          } text-gray-300 mr-3 h-6 w-6`}
                          xmlns="http://www.w3.org/2000/svg"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth="2"
                            d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"
                          />
                        </svg>
                        Quizzes
                      </a>
                    </Link>

                    {/* <a
                      href="#"
                      className="text-gray-300 hover:bg-gray-700 hover:text-white group flex items-center px-2 py-2 text-sm font-medium rounded-md"
                    >
                      <svg
                        className="text-gray-400 group-hover:text-gray-300 mr-3 h-6 w-6"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                        />
                      </svg>
                      Calendar
                    </a> */}

                    {/* <a
                      href="#"
                      className="text-gray-300 hover:bg-gray-700 hover:text-white group flex items-center px-2 py-2 text-sm font-medium rounded-md"
                    >
                      <svg
                        className="text-gray-400 group-hover:text-gray-300 mr-3 h-6 w-6"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        aria-hidden="true"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
                        />
                      </svg>
                      Reports
                    </a> */}
                  </nav>
                </div>
              </div>
            </div>
          </div>
          <div className="flex flex-col w-0 flex-1 overflow-hidden">
            <Navbar />
            <main
              className="flex-1 relative overflow-y-auto focus:outline-none"
              tabIndex="0"
            >
              <div className="py-6">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
                  {/* Replace with your content */}
                  <div className="py-4">{children}</div>
                  {/* /End replace */}
                </div>
              </div>
            </main>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}
