document.querySelector("button#start").addEventListener("click", () => {
  const text = document.querySelector("#calculation").value;

  if(text.includes("+")) {
    const nums = text.split("+");
    const result = nums.reduce((acc, num) => acc + parseInt(num), 0);
    document.querySelector("#result").textContent = result;
  } else if(text.includes("-")) {
    const nums = text.split("-");
    const result = nums.reduce((acc, num) => acc - parseInt(num));
    document.querySelector("#result").textContent = result;
  } else if(text.includes("*")) {
    const nums = text.split("*");
    const result = nums.reduce((acc, num) => acc * parseInt(num));
    document.querySelector("#result").textContent = result;
  } else if(text.includes("/")) {
    const nums = text.split("/");
    const result = nums.reduce((acc, num) => acc / parseInt(num));
    document.querySelector("#result").textContent = result;
  }
});