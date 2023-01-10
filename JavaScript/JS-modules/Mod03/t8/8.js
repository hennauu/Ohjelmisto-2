document.querySelector("button").addEventListener("click", e => {
  const num1 = parseInt(document.querySelector("#num1").value);
  const num2 = parseInt(document.querySelector("#num2").value);
  const operation = document.querySelector("#operation").value;
  const result = document.querySelector("#result");

  if(operation == "add") result.textContent = num1 + num2;
  else if(operation == "sub") result.textContent = num1 - num2;
  else if(operation == "multi") result.textContent = num1 * num2;
  else if(operation == "div") result.textContent = num1 / num2;
});