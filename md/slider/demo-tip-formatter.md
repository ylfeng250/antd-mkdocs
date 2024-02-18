## zh-CN

使用 `tooltip.formatter` 可以格式化 `Tooltip` 的内容，设置 `tooltip.formatter={null}`，则隐藏 `Tooltip`。

## en-US

Use `tooltip.formatter` to format content of `Tooltip`. If `tooltip.formatter` is null, hide it.
```tsx
import React from 'react';
import { Slider } from 'antd';

const formatter = (value: number) => `${value}%`;

const App: React.FC = () => (
  <>
    <Slider tooltip={{ formatter }} />
    <Slider tooltip={{ formatter: null }} />
  </>
);

export default App;
```
