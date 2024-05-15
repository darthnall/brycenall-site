/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./home/templates/home/*.html", "./home/templates/home/**/*.html"],
	theme: {
		extend: {
			colors: {
				"bryce-violet": "#3d2b56",
				"bryce-blue": "#2c497f",
				"bryce-gray": "#808a9f",
				"bryce-green": "#ccf5ac",
				"bryce-green-accent": "#bad29f",
			},
		},
	},
	plugins: [],
};
