## zh-CN

value 和 onChange 需要配合使用。

## en-US

`value` and `onChange` should be used together,
```tsx
import React, { useState } from 'react';
import type { Dayjs } from 'dayjs';
import { TimePicker } from 'antd';

const App: React.FC = () => {
  const [value, setValue] = useState<Dayjs | null>(null);

  const onChange = (time: Dayjs) => {
    setValue(time);
  };

  return <TimePicker value={value} onChange={onChange} />;
};

export default App;
```
