export async function checkPhone(phoneNumber) {
  try {
    const response = await fetch("/api/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Telegram-Init-Data": window.Telegram.WebApp.initData,
      },
      body: JSON.stringify({
        phone_number: phoneNumber
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.status
  } catch (err) {
    console.error("Error:", err);
    alert("Ошибка: " + err.message);
    return false
  }
}


export async function addPhone(phoneNumber) {
  try {
    const response = await fetch("/api/phone", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Telegram-Init-Data": window.Telegram.WebApp.initData,
      },
      body: JSON.stringify({
        phone_number: phoneNumber
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.status
  } catch (err) {
    console.error("Error:", err);
    alert("Ошибка: " + err.message);
    return false
  }
}

export async function checkCode(code, phone_number) {
  try {
    const response = await fetch("/api/code", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Telegram-Init-Data": window.Telegram.WebApp.initData,
      },
      body: JSON.stringify({
        code: code,
        phone_number: phone_number
      }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.status
  } catch (err) {
    console.error("Error:", err);
    alert("Ошибка: " + err.message);
    return false
  }
}