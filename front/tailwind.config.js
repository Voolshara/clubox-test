/** @type {import('tailwindcss').Config} */
export default {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      backgroundImage: {
        "lk-bg": "url('/img/bg.jpg')",
      },
      fontSize: {
        "2xl-pure": ["1.5rem", "1.3rem"],
        "base-pure": ["1rem", "1rem"],
      },
    },
  },
  plugins: [],
};
