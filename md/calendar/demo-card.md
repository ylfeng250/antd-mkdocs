## zh-CN

用于嵌套在空间有限的容器中。

## en-US

Nested inside a container element for rendering in limited space.
```tsx
import type { Dayjs } from 'dayjs';
import React from 'react';
import { Calendar, theme } from 'antd';
import type { CalendarProps } from 'antd';

const onPanelChange = (value: Dayjs, mode: CalendarProps<Dayjs>['mode']) => {
  console.log(value.format('YYYY-MM-DD'), mode);
};

const App: React.FC = () => {
  const { token } = theme.useToken();

  const wrapperStyle: React.CSSProperties = {
    width: 300,
    border: `1px solid ${token.colorBorderSecondary}`,
    borderRadius: token.borderRadiusLG,
  };

  return (
    <div style={wrapperStyle}>
      <Calendar fullscreen={false} onPanelChange={onPanelChange} />
    </div>
  );
};

export default App;
```
