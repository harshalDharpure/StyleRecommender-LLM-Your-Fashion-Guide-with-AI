document.addEventListener("DOMContentLoaded", () => {
    const recommendButton = document.getElementById("recommendButton");
    const userInput = document.getElementById("userInput");
    const recommendations = document.getElementById("recommendations");

    recommendButton.addEventListener("click", () => {
        const userText = userInput.value;
        fetch("/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ user_input: userText }),
        })
        .then((response) => response.json())
        .then((data) => {
            recommendations.innerHTML = `Recommendation: ${data.recommendation}`;
        });
    });
});
